<template>
<el-container>
 <el-row :gutter="20" style="width:1600px">
  <el-col :span="12" :offset="6">
      
         
      <el-card class="box-card" style="min-height:200px;margin-top:50px">
          <el-form ref="form" :model="form">
              <el-form-item label="项目名称" prop="projectname">
                    <el-input v-model="form.projectname"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="onAddProject">保存</el-button>
                <el-button type="primary" @click="onCancel">取消</el-button>
            </el-form-item>
          </el-form>
      </el-card>
  </el-col>
</el-row>
</el-container>
</template>
<script>
import {addproject} from '../service/getdata'
export default {
    name:'AddProject',
    data(){
        return {
            form:{
                projectname:""
            }
        }
    },
    methods:{
        async onAddProject(){
            let rep = await addproject(this.form.projectname)
            if (rep.info)
                this.$router.push('/projectlist')
        },
        onCancel(){
            this.$router.go(-1);
        }
    }
}
</script>
