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
        <el-menu-item index="1" @click="openLoginDialog">
          <template #title>登录</template>
        </el-menu-item>
        
        <el-dialog v-model="loginDialogVisible" title="欢迎回来" style="width: 800px;">
          <el-form v-model="loginForm">
            <el-form-item label="手机号" label-width="100px">
              <el-input v-model="loginForm.tel" placeholder="请输入手机号" />
            </el-form-item>
            <el-form-item label="密码" label-width="100px">
              <el-input v-model="loginForm.password" placeholder="请输入密码" show-password="true"/>
            </el-form-item>
          </el-form>
          <template #footer>
            <el-button type="primary" @click="login">登录</el-button>
          </template>
        </el-dialog>

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

const loginDialogVisible = ref(false);
const openLoginDialog = () => {
  loginDialogVisible.value = true;
}

const loginForm = reactive({
  tel: '', password: ''
})

const login = () => {
  console.log(loginForm.value);
  loginDialogVisible.value = false;
  ElMessage.success('登录成功');
}

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
