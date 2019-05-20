<template>
<el-container>
  <el-header>
    <el-row :gutter="20">
        <el-col :span="6" class="logo" align="left">
            <div style="padding-left:30px">
            <router-link to="/mainpage" style="color:#fff;font-weight:bold">InnerBug</router-link>
            </div>
            </el-col>
        <el-col :span="6" :offset="12"><div class="grid-content bg-purple"  text-align="right">
        <right-drop v-bind:user-name="userName" v-bind:is-admin="isAdmin"></right-drop>
        </div>
        </el-col>
    </el-row>
  </el-header>
    <router-view></router-view>
  
</el-container>
</template>
<script>
import RightDrop from "./common/RightDrop"
export default {
    name:"Main",
    data(){
        return {
            userName:this.$store.state.username,
            isAdmin:this.$store.state.isadmin
        }
    },
    components:{
            'right-drop':RightDrop
    }
}
</script>
<style scoped>
   .el-header{
       background-color: #303133;
       color: #ffffff;
       line-height:60px;
   }
</style>

