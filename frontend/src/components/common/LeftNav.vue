<template>
<el-menu  :default-active="$route.path"
                class="el-menu-vertical-demo" 
                background-color="#303133"
                
      text-color="#fff"
      active-text-color="#ffd04b"
      router
      >
                <el-menu-item v-for="(item,index) in items" :index="getUrl(item.id)" align="left">
                    <span slot="title" >{{item.projectname}}</span>
                </el-menu-item>
</el-menu>
</template>
<script>
import {getprojectlist} from '../../service/getdata'
export default {
    data(){
        return {
            items:[]
        }
    },
    created(){
        this.initData()
    },
    methods:{
        toProject(id){
            console.log(id)
            this.$router.push('/buglist/'+id)
        },
        getUrl(id){
            return "/buglist/"+id
        },
        async initData(){
            this.items = await getprojectlist()
            
        }
    }

}
</script>
<style scoped>
.el-menu-vertical-demo{
    min-height: 800px;
    
}
</style>

