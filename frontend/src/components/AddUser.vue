<template>
<el-container>
 <el-row :gutter="20" style="width:1600px">
  <el-col :span="12" :offset="6">
      
         
      <el-card class="box-card" style="min-height:200px;margin-top:50px">
          <el-form ref="form" :model="form">
              <el-form-item label="用户姓名" prop="username">
                    <el-input v-model="form.username"></el-input>
              </el-form-item>
              <el-form-item label="登录名" prop="loginname">
                    <el-input v-model="form.loginname"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                    <el-input v-model="form.password" type="password"></el-input>
              </el-form-item>
                <el-form-item label="权限">
              <template>
                <el-radio v-model="form.isadmin" label="true">管理员</el-radio>
                <el-radio v-model="form.isadmin" label="false">普通用户</el-radio>
                </template>
                </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="onAddUser">保存</el-button>
                <el-button type="primary" @click="onCancel">取消</el-button>
            </el-form-item>
          </el-form>
      </el-card>
  </el-col>
</el-row>
</el-container>
</template>
<script>
import {adduser} from '../service/getdata'
export default {
    data(){
        return {
            form:{
                username:"",
                loginname:"",
                password:"",
                isadmin:"true"
            }
        }
    },
    name:'AddUser',
    methods:{
        async onAddUser(){
            let rep = await adduser(this.form.username,this.form.loginname,this.form.password,this.form.isadmin)
            if (rep.info)
                this.$router.go(-1)
        },
        onCancel(){
            this.$router.go(-1);
        }
    }
}
</script>
