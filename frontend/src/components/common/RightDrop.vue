<template>
<el-dropdown trigger="click">
        <span class="el-dropdown-link" style="color:#fff">
        {{userName}}<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item icon="el-icon-plus" @click.native="addBug">新建BUG</el-dropdown-item>
        <el-dropdown-item icon="el-icon-s-custom" v-if="isAdmin" @click.native="userList">人员管理</el-dropdown-item>
        <el-dropdown-item icon="el-icon-document" v-if="isAdmin" @click.native="prjList">项目管理</el-dropdown-item>
        <el-dropdown-item icon="el-icon-s-tools" @click.native="changePass">修改密码</el-dropdown-item>
        <el-dropdown-item icon="el-icon-s-platform" @click.native="logOut">退出登录</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
</template>
<script>
export default {
    props:['userName','isAdmin'],
    data(){
        return {
            
        }
    },
    methods:{
      changePass(){
        this.$router.push('/changepass')
      },
      addBug(){
        this.$router.push('/addbug')
      },
      logOut(){
        this.$store.dispatch('UserLogout')
        this.$router.push('/login')
      },
      prjList(){
        this.$router.push('/projectlist')
      },
      userList(){
        this.$router.push('/userlist')
      }
    }
}
</script>

