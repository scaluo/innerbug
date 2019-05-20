<template>
<div>
<el-row :gutter="20" style="margin-top:100px;">
  <el-col :span="14" :offset="5">
      <el-card class="box-card" style="min-height:400px">
  <div slot="header" class="clearfix">
      <span>用户列表</span>
    <el-button style="float: right; padding: 3px 0" type="text" @click="newUser">新增用户</el-button>
  </div>
    <el-table
        :data="tableData"
        stripe
        border
        v-loading="loading"
        :row-style="rowStyle"
        :header-row-style="headerRowStyle"
        :header-cell-style="headerCellStyle"
        :cell-style="cellStyle"
        style="width: 100%"
        >
        <el-table-column
        prop="username"
        label="姓名"
        >
        </el-table-column>
        <el-table-column
        prop="loginname"
        label="登录名"
        >
        </el-table-column>
        <el-table-column
        prop="isadmin"
        label="角色"
        >
        <template slot-scope="scope">
                {{scope.row.isadmin|roledesc}}
            </template>
        </el-table-column>
        <el-table-column
        label="操作"
        width="50">
        <template slot-scope="scope">
        <el-button @click="onDelUser(scope.$index,scope.row)" type="text" size="small">删除</el-button>
        
      </template>
        </el-table-column>
         <el-table-column
        prop="id"
        label="id"
        v-if="false">
        </el-table-column>
    </el-table>
    </el-card>
     
  </el-col>
    </el-row>
  </div>
</template>
<script>
import {getuserlist,deluser} from '../service/getdata'
export default {
    data(){
        return {
            tableData:[],
            loading:true
        }
    },
    created(){
        this.initData()
    },
    methods:{
        rowStyle(){
          return "height:35px;"
        },
        cellStyle(){
            return "padding:0;"
        },
        headerRowStyle(){
          return "height:45px;"
        },
        headerCellStyle(){
          return "padding:0px"
        },
        async initData(){
            
            this.tableData = await getuserlist()
            this.loading = false
            
        },
        async onDelUser(index,row){
            if(confirm("确实要删除吗？"))
            {
                let rep = await deluser(row.id)
                if (rep.info)
                    this.tableData.splice(index,1)
            }
        },
        newUser(){
            this.$router.push('/adduser')
        }

    }
}
</script>
