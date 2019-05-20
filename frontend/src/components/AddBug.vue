<template>
<el-container>
 <el-row :gutter="20" style="width:1600px">
  <el-col :span="12" :offset="6">
      
          <h2>新增BUG</h2>
           <el-card class="box-card">
          <el-form ref="form" :model="form" label-width="80px">
              <el-form-item label="错误标题" prop="title">
                    <el-input v-model="form.title"></el-input>
              </el-form-item>
              <el-form-item label="重要程度" prop="level"  style="text-align:left;">
                    <el-select v-model="form.level" placeholder="请选择">
                    <el-option v-for="item in form.levels"
                        :key="item.value"
                        :label="item.value"
                        :value="item.value">
                    </el-option>
              </el-select>
              </el-form-item>
              <el-form-item label="所属项目" prop="prj"  style="text-align:left;">
                    <el-select v-model="form.prj" placeholder="请选择">
                    <el-option v-for="item in form.prjs"
                        :key="item.id"
                        :label="item.projectname"
                        :value="item.id">
                    </el-option>
                    </el-select>
              </el-form-item>
              <el-form-item label="错误详情" prop="content">
                  <el-input
                    type="textarea"
                    :rows="6"
                    placeholder="请输入内容"
                    v-model="form.content">
                    </el-input>
              </el-form-item>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="onAddBug">保存</el-button>
            </el-form-item>
          </el-form>
       </el-card>
  </el-col>
</el-row>
</el-container>
</template>
<script>
import {getprojectlist,addbug} from '../service/getdata'
export default {
    data(){
        return {
            form:{
                title:'',
                level:'',
                levels:[
                    {value:'一般'},
                    {value:'重要'},
                    {value:'紧急'}
                ],
                content:'',
                prj:'',
                prjs:[]
            }
        }
    },
    created(){
        this.initData()
    },
    methods:{
        async initData(){
            this.form.prjs = await getprojectlist()
        },
        async onAddBug(){
            let _this = this
            let prjid = this.form.prj
            let rep = await addbug(this.form.title,this.form.level,this.form.prj,this.form.content)

            _this.$router.push('/buglist/'+prjid)
        }
    }
}
</script>
