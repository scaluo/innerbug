import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Main from '@/components/Main'
import MainPage from '@/components/MainPage'
import BugList from '@/components/BugList'
import MainProject from '@/components/MainProject'
import ChangePass from '@/components/ChangePass'
import AddProject from '@/components/AddProject'
import AddUser from '@/components/AddUser'
import AddBug from '@/components/AddBug'
import ProjectList from '@/components/ProjectList'
import UserList from '@/components/UserList'
import EdtBug from '@/components/EdtBug'
import NotFound from '@/components/errors/NotFound'
import store from '../store'
Vue.use(Router)

const router =  new Router({
  routes: [
    {
      path:'/',
      redirect:'/mainpage'
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {
        isLogin:false,
        title:'用户登录'
      }
     },
    {
      path: '/main',
      name:'Main',
      component:Main,
      meta:{
        isLogin:true
      },
      children:[
        {
          path: '/changepass',
          name:'ChangePass',
          component:ChangePass,
          meta:{
            isLogin:true,
            title:'修改密码'
          }
        },
        {
          path: '/addproject',
          name:'AddProject',
          component:AddProject,
          meta:{
            isLogin:true,
            title:'新增项目'
          }
        },
        {
          path: '/projectlist',
          name:'ProjectList',
          component:ProjectList,
          meta:{
            isLogin:true,
            title:'项目列表'
          }
        },
        {
          path: '/adduser',
          name:'AddUser',
          component:AddUser,
          meta:{
            isLogin:true,
            title:'新增用户'
          }
        },
        {
          path: '/userlist',
          name:'UserList',
          component:UserList,
          meta:{
            isLogin:true,
            title:'用户列表'
          }
        },
        {
          path: '/mainproject',
          name:'MainProject',
          component:MainProject,
          meta:{
          isLogin:true
          },
          children:[
            {
              path:'/mainpage',
              name:'MainPage',
              component:MainPage,
              meta:{
                isLogin:true,
                title:'首页'
              }
          },
          {
              path:'/buglist/:prjid',
              name:'BugList',
              component:BugList,
              props:true,
              meta:{
                isLogin:true,
                title:'BUG列表'
              }
          },
          {
            path: '/addbug',
            name:'AddBug',
            component:AddBug,
            meta:{
              isLogin:true,
              title:'新增bug'
            }
          },
          {
            path:'/edtbug/:id',
            name:'EdtBug',
            component:EdtBug,
            meta:{
              isLogin:true,
              title:'修改BUG'
            }
        }
          ]
        }
      ]
      
    },
    {
      path:'*',
      name:'NotFound',
      component:NotFound
    }
  ]
})

router.beforeEach((to, from, next) => {
  let token = store.state.token;
  if (to.meta.isLogin) {
   if (token) {
     next();
    } else {
     next({
      path: '/login',
      query: { redirect: to.fullPath } // 将刚刚要去的路由path作为参数，方便登录成功后直接跳转到该路由
     });
    }
   } else {
    next(); 
   }
  });

  router.afterEach((to, from, next) => {
    if (to.meta.title) {
        document.title = 'innerbug--'+to.meta.title;
    }
    //next();
  });

  export default router;
