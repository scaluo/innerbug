<template>
<el-container>
 <el-row :gutter="20" style="width:1600px">
  <el-col :span="12" :offset="6">
          <h2>BUG当前状态：{{form.status|statusdesc}}</h2>

          <el-card class="box-card"  v-loading="loading">
          <el-form :label-position="labelPosition" ref="form" :model="form" label-width="80px">
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
              <el-form-item label="所属项目" prop="prj" style="text-align:left;">
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
              
              <el-form-item >
                <el-button type="primary" @click="onEdtBug" v-if="form.status==0">保存修改</el-button>
                <el-button type="primary" @click="onSetStatus(1)" v-if="form.status==0">开始解决</el-button>
                <el-button type="primary" @click="onSetStatus(2)" v-if="form.status<2">已修复</el-button>
                  <el-button type="primary" @click="onDelBug()">删除BUG</el-button>
              </el-form-item>
          </el-form>
      </el-card>
  </el-col>
</el-row>
</el-container>
</template>
<script>
import {getbug,setbugstatus,updatebug,getprojectlist,delbug} from '../service/getdata'
export default {
    data(){
        return {
            loading:true,
            labelPosition:'left',
            form:{
                id:0,
                title:'',
                level:'',
                levels:[
                    {value:'一般'},
                    {value:'重要'},
                    {value:'紧急'}
                ],
                content:'',
                prj:'',
                prjs:[],
                status

            }
        }
    },
    created(){
        this.initData()
    },
    methods:{
        async initData(){
            let _this = this
            let id = this.$route.params.id
            let rep = await getbug(id)
            _this.form.id=rep.id
            _this.form.title = rep.title
            _this.form.status = rep.status
            _this.form.content = rep.content
            _this.form.level = rep.level
            _this.form.prj = rep.project_id
            _this.form.prjs = await getprojectlist()
            _this.loading = false
        },
        async onSetStatus(status){
            let _this=this
            
            let rep = await setbugstatus(this.form.id,status)
            if (rep.info)
                _this.$router.push('/buglist/'+_this.form.prj)

        },
        async onEdtBug(){
            let _this = this
           
            let rep=await  updatebug(this.form.id,this.form.title,this.form.prj,this.form.level,this.form.content)
            if (rep.info)
                _this.$router.push('/buglist/'+_this.form.prj)
        },
        async onDelBug(){
            if(confirm("确实要删除吗？"))
            {
                let _this = this
                let rep=await  delbug(this.form.id)
                if (rep.info)
                    _this.$router.push('/buglist/'+_this.form.prj)
            }
        }
    }
}
</script>
