<template>
    <div>
    
  <el-row :gutter="20" style="margin-top:100px;">
  <el-col :span="14" :offset="5">
      <el-card class="box-card" style="min-height:400px">
  <div slot="header" class="clearfix">
      <span>项目列表</span>
    <el-button style="float: right; padding: 3px 0" type="text" @click="newProject">新增项目</el-button>
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
        prop="projectname"
        label="项目名称"
        >
        </el-table-column>
        <el-table-column
        prop="ctime"
        label="创建日期"
        width="180">
        </el-table-column>
        <el-table-column
        label="操作"
        width="50">
        <template slot-scope="scope">
        <el-button @click="onDelPrj(scope.$index,scope.row)" type="text" size="small">删除</el-button>
        
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
import {getprojectlist,delprj} from '../service/getdata'
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
            return "padding:0"
        },
        headerRowStyle(){
          return "height:45px;"
        },
        headerCellStyle(){
          return "padding:0px"
        },
        async initData(){
            
            this.tableData = await getprojectlist()
            this.loading = false
            
        },
        newProject(){
            this.$router.push('/addproject')
        },
        
        async onDelPrj(index,row){
            
            if(confirm("确实要删除吗？"))
            {
                let rep = await delprj(row.id)
                if (rep.info)
                    this.tableData.splice(index,1)
            }
        }
    }

}
</script>

