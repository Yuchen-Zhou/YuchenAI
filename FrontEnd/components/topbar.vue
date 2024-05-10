<template>
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
    >
      <el-menu-item index="0">
        <img src="@/assets/logo/logo1.png" width="150px" height="200px">
      </el-menu-item>

      <div class="flex-grow" />
      <NuxtLink to="/login">
        <el-menu-item index="1">
          <template #title>登录/注册</template>
        </el-menu-item>
      </NuxtLink>
  
      
    </el-menu>
</template>
  
<script lang="ts" setup>
import { ref, onMounted } from 'vue';

onMounted(() => {
  
});
</script>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>
