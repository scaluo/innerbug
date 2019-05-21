<template>
<el-row :gutter="20" style="margin-top:100px;">
  <el-col :span="12" :offset="6">
      <div class="grid-content bg-purple">
          <el-card class="box-card">
          <h2>用户登录</h2>
          <el-form ref="form" :model="form" :rules="rules" label-width="80px">
              <el-form-item label="登录名" prop="name">
                    <el-input v-model="form.name"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="pass">
                    <el-input type="password" v-model="form.pass" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="onLogin">登录</el-button>
            </el-form-item>
          </el-form>
          </el-card>
      </div>
  </el-col>
</el-row>
</template>
<script>
import { login } from '../service/getdata'
export default {
    name:'Login',
    data(){
        return {
            form:{
                name:'',
                pass:''
            },
            rules:{
                name:[
                    {required:true,message:'请输入登录名',trigger:'change'}
                ],
                pass:[
                    {required:true,message:'请输入密码',trigger:'blur'}
                ]
            }

        }
    },
    methods:{
       async onLogin(){
           let _this = this
           if (_this.form.name===""||_this.form.pass==="")
            {
                alert("用户名密码不能为空")
            }
            else
            {
                let rep = await login(_this.form.name,_this.form.pass)
                if (rep.message)
                    alert(rep.message)
                else
                {
                console.log(rep)
                _this.$store.dispatch('UserLogin',rep)
                _this.$router.push('/mainpage')
                }
            }
         }
    }
    
}
</script>
<style scoped>

</style>

