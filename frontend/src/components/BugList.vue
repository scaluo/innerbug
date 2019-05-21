<template>
  <div>
    
    <el-table
        @row-click="openDetails"
        :data="tableData"
        border
        v-loading="loading"
        style="width: 100%"
        :row-style="rowStyle"
        :header-row-style="headerRowStyle"
        :header-cell-style="headerCellStyle"
        :cell-style="cellStyle"
        :row-class-name="tableRowClassName">
        <el-table-column
        prop="title"
        label="标题">
        </el-table-column>
        <el-table-column
        prop="level"
        label="重要性"
        width="180"
        >
        </el-table-column>
        <el-table-column
        prop="ctime"
        sortable
        label="创建日期"
        width="180">
        </el-table-column>
        <el-table-column
        label="状态"
        width="180"
        prop="status"
        :filters="[{ text: '未开始', value: 0 }, { text: '进行中', value: 1 },{ text: '已完成', value: 2 }]"
        :filter-method="filterTag"
        >
            <template slot-scope="scope">
                {{scope.row.status|statusdesc}}
            </template>
        </el-table-column>

        <el-table-column
        prop="id"
        label="id"
        v-if="false">
        </el-table-column>
        
    </el-table>
  </div>
</template>
<script>
import {getbuglist} from "../service/getdata"
export default {
    
    data() {
        return {
            tableData:[],
            loading:true
        }
    },
    props:['prjid'],
    created(){
      
        this.initData()
    },
    methods:{
         handleClick(row) {
            console.log(row);
        },
        openDetails(row){
            this.$router.push('/edtbug/'+row.id)
        },
        rowStyle(){
          return "height:35px;"
        },
        cellStyle(){
            return "padding:0;cursor:pointer;"
        },
        headerRowStyle(){
          return "height:45px;"
        },
        headerCellStyle(){
          return "padding:0px"
        },
        async initData(){
            this.tableData = await getbuglist(this.prjid)
            this.loading = false;
         
        },
        tableRowClassName({row, rowIndex}) {
        if (row.status === 1) {
          return 'warning-row';
        } else if (row.status === 2) {
          return 'success-row';
        }
        return '';
        },
        filterTag(value, row) {
        console.log(row.status)
        return row.status === value;
      }
    },
    watch:{
        
        prjid(){
            this.initData()
        }
    }
}
</script>
<style>
  .el-table .warning-row {
    background: oldlace;
    
  }

  .el-table .success-row {
    background: #f0f9eb;
  }

  td{
      height:30px;
  }

</style>

