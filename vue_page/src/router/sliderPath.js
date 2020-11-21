import abstract from '@/views/common/abstract.vue'
import Project from '@/views/promanage/project.vue'
import funcSuite from '@/views/funcModule/funcSuite.vue'
import workFlow from  '@/views/workFlow/case.vue'

export default [
        {
          path:'/promanage',
          name:'promanage',
          meta:{
            name:'项目管理'
          },
          component:abstract,
          children:[
            {
              path:'project',
              name:'project',
              meta:{
                name:'项目',
              },
              component:Project,
            }
          ]
        },

        {
          path:'/funcModule',
          name:'funcModule',
          meta:{
            name:'功能模块'
          },
          component:abstract,
          children:[
            {
              path:'funcSuite',
              name:'funcSuite',
              meta:{
                name:'模块',
              },
              component:funcSuite,
            }
          ]
        },

        {
          path:'/workFlow',
          name:'workFlow',
          meta:{
            name:'业务明细'
          },
          component:abstract,
          children:[
            {
              path:'case',
              name:'case',
              meta:{
                name:'业务流',
              },
              component:workFlow,
            }
          ]
        },
  ]
