<template>
<el-container>
        <el-aside width="200px" style="background-color:#303133">
            <left-nav></left-nav>
        </el-aside>
        <el-main>
            <router-view>
                <div></div>
            </router-view>
        </el-main>
    </el-container>
</template>
<script>
import LeftNav from "./common/LeftNav"
export default {
    name:"MainProject",
    
    components:{
                LeftNav
    
                }
}
</script>