<template>
<el-container>
 <el-row :gutter="20" style="width:1600px">
  <el-col :span="12" :offset="6">
      
          <h2>修改密码</h2>
          <el-form ref="form" :model="form">
              <el-form-item label="原密码" prop="oldpassword">
                    <el-input type="password" v-model="form.oldpassword"></el-input>
              </el-form-item>
              <el-form-item label="新密码" prop="newpassword">
                    <el-input type="password" v-model="form.newpassword" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="onChangePass">修改密码</el-button>
            </el-form-item>
          </el-form>
      
  </el-col>
</el-row>
</el-container>
</template>
<script>
import {changepassword} from '../service/getdata'
export default {
    name:"ChangePass",
    data(){
        return {
             form:{
                oldpassword:'',
                newpassword:''
            }
        }
    },
    methods:{
        async onChangePass(){
            
            let rep = await changepassword(this.form.oldpassword,this.form.newpassword)
            if (rep.info)
                alert(rep.info)
        }
    }
}
</script>

