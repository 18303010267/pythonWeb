<template>
<div class="project">
<el-row display="margin-top:10px">
<el-input v-model="input" placeholder="请输入模块名" style="display:inline-table; width: 30%; float:left"></el-input>
 <el-button type="primary" @click="showFuncSuite()"  style="float:left; margin: 2px;">查询</el-button>

<!-- Form 新增弹框-->
<el-button type="text" @click="dialogFormVisible = true" style="float:left; margin-left: 40px;">新增</el-button>

<el-dialog title="新增模块" :visible.sync="dialogFormVisible">
  <el-form :model="form">

    <el-form-item label="所属项目" :label-width="formLabelWidth">
        <template>
          <el-select v-model="pk_add" placeholder="请选择" filterable  style="margin-left:-320px;">
            <el-option  style="width:100px;display:block;"
              v-for="item in options"
              :key="item.pk"
              :label="item.fields.name"
              :value="item.pk">
            </el-option>
          </el-select>
        </template>
    </el-form-item>

    <el-form-item label="模块名称" :label-width="formLabelWidth">
      <el-input v-model="form.name" autocomplete="off"   style="width:320px;margin-left: -190px;"></el-input>
    </el-form-item>

  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">取 消</el-button>
    <el-button type="primary" @click="addSuite()">确 定</el-button>
  </div>
</el-dialog>
<!-- Form -->

</el-row>


<el-row>
<el-table :data="proList" style="width: 100%" border>
<el-table-column  label="编号" min-width="30">
<template slot-scope="scope"> {{ scope.row.suite_id }} </template>
</el-table-column>
<el-table-column  label="项目名" min-width="30">
<template slot-scope="scope"> {{ scope.row.project_id__name }} </template>
</el-table-column>
<el-table-column  label="模块名" min-width="30">
<template slot-scope="scope"> {{ scope.row.name}} </template>
</el-table-column>
 <el-table-column
      fixed="right"
      label="操作"
      width="150">
      <template slot-scope="scope">

        <el-button size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
        <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
</el-table>
    </el-row>





 <!-- Form 修改弹框-->

<el-dialog title="修改项目" :visible.sync="editVisible">
  <el-form :model="editForm">

    <el-form-item label="所属项目" :label-width="formLabelWidth">
        <template>
          <el-select v-model="pk" placeholder="请选择" filterable  style="margin-left:-320px;">
            <el-option  style="width:100px;display:block;"
              v-for="item in options"
              :key="item.pk"
              :label="item.fields.name"
              :value="item.pk">
            </el-option>
          </el-select>
        </template>
   </el-form-item>

   <el-form-item label="模块名称" :label-width="formLabelWidth">
      <el-input v-model="editForm.name" autocomplete="off"   style="width:320px;margin-left: -190px;"></el-input>
    </el-form-item>

  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="editVisible = false">取 消</el-button>
    <el-button type="primary" @click="editSuite()">确 定</el-button>
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
      baseUrl:'http://127.0.0.1:8000',
      input: '',
      proList: [],  //存放模块信息
      options:[], //定义项目列表下拉框
      pk:'',  //项目修改框的主键
      pk_add:'', //项目添加框的主键
      dialogFormVisible: false,
        form: {
          name: ''
        },
        editForm:{
          name:'',
        },
        formLabelWidth: '80px',
        delVisible: false,//删除提示弹框的状态
        editVisible:false,//修改提示弹框的状态

        msg: "",//记录每一条的信息，便于取id
        delarr: "",//存放删除的数据
        ids:""//存放修改数据的ids

    }
  },
  mounted: function () {

    this.showFuncSuite();
    this.showProjects();

  },
  methods: {

    handleClick(row) {
        console.log(row);
      },


    //模块展示
    showFuncSuite () {
      this.$http.get(this.baseUrl+'/api/show_FuncSuite?name=' + this.input)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.proList = res['list']
            console.log(this.proList)
          } else {
            this.$message.error('查询模块失败')
            console.log(res['msg'])
          }
        })
    },

     //下拉框加载项目信息
     showProjects () {
      this.$http.get(this.baseUrl+'/api/show_projects?name=')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.options = res['list']
          } else {
            console.log(res['msg'])
          }
        })
    },

    addSuite(){

      this.dialogFormVisible = false,
      this.$http.post(this.baseUrl+'/api/add_suite',{pk:this.pk_add,name:this.form.name},{emulateJSON:true})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.form.name=""
            this.pk_add = ""
            this.showFuncSuite()
          } else {
            this.$message.error('添加模块失败')
            console.log(res['msg'])
          }
        })
    },
     //修改框回显数据
    handleEdit(index,row){
    this.editVisible = true
    this.editForm.name=row.name
    this.pk=row.project_id__project_id   //项目id
    this.ids = row.suite_id


    },

    //修改模块
    editSuite(){
      this.editVisible = false,
      this.$http.post(this.baseUrl+'/api/edit_suite',{suite_id:this.ids,name:this.editForm.name,project_id:this.pk},{emulateJSON:true})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.form.name=""
            this.form.url=""
            this.showFuncSuite()
          } else {
            this.$message.error('修改项目失败')
            console.log(res['msg'])
          }
        })
    },
     //单行删除

    handleDelete(index, row) {

      this.idx = index;

      this.msg = row;//每一条数据的对象

      this.delarr = this.msg.suite_id;//把单行删除的每条数据的id添加进放删除数据的数组
      console.log(this.delarr)

      this.delVisible = true;

    },

     // 确定删除
    deleteRow() {
      this.$http.get(this.baseUrl+'/api/del_suite?suite_id='+this.delarr

      ).then((response) => {
           var res = JSON.parse(response.bodyText)


       if (res.error_num === 0) {

          this.$message.success('删除成功')

          this.showFuncSuite()

        }else{

        console.log(res['msg'])

        this.$message.error('删除失败')

      }

      }),

      this.delVisible = false;//关闭删除提示模态框

    },







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
