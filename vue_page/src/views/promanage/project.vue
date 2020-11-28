<template>
<div class="project">
<el-row display="margin-top:10px">
<el-input v-model="input" placeholder="请输入项目名" style="display:inline-table; width: 30%; float:left"></el-input>
 <el-button type="primary" @click="showProjects()"  style="float:left; margin: 2px;">查询</el-button>
<!--el-button type="primary" @click="addBook()" style="float:left; margin: 20px;">新增</el-button-->

<!-- Form 新增弹框-->
<el-button type="text" @click="dialogFormVisible = true" style="float:left; margin-left: 40px;">新增</el-button>

<el-dialog title="新增项目" :visible.sync="dialogFormVisible">
  <el-form :model="form">
    <el-form-item label="项目名称" :label-width="formLabelWidth">
      <el-input v-model="form.name" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="baseUrl" :label-width="formLabelWidth">
      <el-input v-model="form.url" autocomplete="off"></el-input>
    </el-form-item>

  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">取 消</el-button>
    <el-button type="primary" @click="addProjects()">确 定</el-button>
  </div>
</el-dialog>
<!-- Form -->

</el-row>


<el-row>
<el-table :data="proList" style="width: 100%" border>
<el-table-column prop="pk" label="编号" min-width="30">
<template slot-scope="scope"> {{ scope.row.pk }} </template>
</el-table-column>
<el-table-column prop="name" label="项目名" min-width="30">
<template slot-scope="scope"> {{ scope.row.fields.name }} </template>
</el-table-column>
<el-table-column prop="url" label="项目接口地址" min-width="30">
<template slot-scope="scope"> {{ scope.row.fields.url }} </template>
</el-table-column>
 <el-table-column
      fixed="right"
      label="操作"
      width="150">
      <template slot-scope="scope">
        <!--el-button @click="handleClick(scope.row)" type="text" size="small">编辑</el-button-->
        <!--el-button type="text" size="small"  @click="handleClick(scope.row)">删除</el-button-->
         <el-button size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>

        <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
</el-table>
    </el-row>





 <!-- Form 修改弹框-->

<el-dialog title="修改项目" :visible.sync="editVisible">
  <el-form :model="editForm">
    <el-form-item label="项目名称" :label-width="formLabelWidth">
      <el-input v-model="editForm.name" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="baseUrl" :label-width="formLabelWidth">
      <el-input v-model="editForm.url" autocomplete="off"></el-input>
    </el-form-item>

  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="editVisible = false">取 消</el-button>
    <el-button type="primary" @click="editProjects()">确 定</el-button>
  </div>
</el-dialog>
<!-- Form -->



    <!-- 删除提示框 -->

  <el-dialog title="提示" :visible.sync="delVisible" width="300px" center>

    <div class="del-dialog-cnt">删除不可恢复，是否确定删除？</div>

    <span slot="footer" class="dialog-footer">

      <el-button @click="delVisible = false">取 消</el-button>

      <el-button type="primary" @click="deleteRow">确 定</el-button>

  </span>

  </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'project',
  data () {
    return {
      //baseUrl:location.hostname+":"+window.location.port, 有跨域问题，后续解决
      baseUrl:'http://127.0.0.1:8000',
      input: '',
      proList: [],
      dialogFormVisible: false,
        form: {
          name: '',
          url: ''

        },
        editForm:{
          name:'',
          url:''
        },
        formLabelWidth: '100px',
        delVisible: false,//删除提示弹框的状态
        editVisible:false,//修改提示弹框的状态

        msg: "",//记录每一条的信息，便于取id


        delarr: "",//存放删除的数据
        ids:""//存放修改数据的ids

    }
  },
  mounted: function () {

    this.showProjects();

  },
  methods: {

    handleClick(row) {
        console.log(row);
      },

    //修改框回显数据
    handleEdit(index,row){
    this.editVisible = true
    this.ids = row.pk
    this.editForm.name=row.fields.name
    this.editForm.url=row.fields.url

    },

      //单行删除

    handleDelete(index, row) {

      this.idx = index;

      this.msg = row;//每一条数据的对象

      this.delarr = this.msg.pk;//把单行删除的每条数据的id添加进放删除数据的数组


      this.delVisible = true;

    },

    // 确定删除

    deleteRow() {
      this.$http.get(this.baseUrl+'/api/del_projects?pk='+this.delarr

      ).then((response) => {
           var res = JSON.parse(response.bodyText)


       if (res.error_num === 0) {

          this.$message.success('删除成功')

          this.showProjects()

        }else{

        console.log(res['msg'])

        this.$message.error('删除失败')

      }

      }),

      this.delVisible = false;//关闭删除提示模态框

    },



    addBook () {
      this.$http.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.input)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.showBooks()
          } else {
            this.$message.error('新增书籍失败，请重试')
            console.log(res['msg'])
          }
        })
    },
    showBooks () {
      this.$http.get('http://127.0.0.1:8000/api/show_books')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.bookList = res['list']
          } else {
            this.$message.error('查询书籍失败')
            console.log(res['msg'])
          }
        })
    },
    showProjects () {
      this.$http.get(this.baseUrl+'/api/show_projects?name=' + this.input)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.proList = res['list']
          } else {
            this.$message.error('查询项目失败')
            console.log(res['msg'])
          }
        })
    },

    addProjects() {
      this.dialogFormVisible = false,
      this.$http.post(this.baseUrl+'/api/add_project',{projectName:this.form.name,url:this.form.url},{emulateJSON:true})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.form.name=""
            this.form.url=""
            this.showProjects()
          } else {
            this.$message.error('添加项目失败')
            console.log(res['msg'])
          }
        })
    },

    editProjects(){
      this.editVisible = false,
      this.$http.post(this.baseUrl+'/api/edit_project',{pk:this.ids,projectName:this.editForm.name,url:this.editForm.url},{emulateJSON:true})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.form.name=""
            this.form.url=""
            this.showProjects()
          } else {
            this.$message.error('修改项目失败')
            console.log(res['msg'])
          }
        })
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
  list-style-type: none;
  padding: 0;
}

  li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
