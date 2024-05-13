<template>
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
    >
      <el-menu-item index="0">
        <NuxtLink to="/">
          <img src="@/assets/logo/logo1.png" width="150px" height="200px">
        </NuxtLink>
      </el-menu-item>



      <div class="flex-grow" />
      <template v-if="!showLogin">
        <NuxtLink to="/users/login">
          <el-menu-item index="2" >
            <template #title>登录</template>
          </el-menu-item>
        </NuxtLink>
        <NuxtLink to="/users/register">
          <el-menu-item index="3">
            <template #title>注册</template>
          </el-menu-item>
        </NuxtLink>
      </template>
      
    </el-menu>
</template>
  
<script lang="ts" setup>
const showLogin = ref(false);
const router = useRouter();

onMounted(() => {

  if (router.currentRoute.value.href !== '/') {
    showLogin.value = true;
  }
});

</script>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>
