<template>
  <div class="common-layout">
    <el-header>
      <Topbar />
    </el-header>
    <el-main>
      <el-row>
        <el-col :span="10" :offset="7">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>注册</span>
            </div>
            <el-form :model="registerForm" label-width="auto" style="max-width: 600px">
              <el-form-item label="手机号: ">
                <el-input v-model="registerForm.phoneNumber" placeholder="请输入你的手机号"/>
              </el-form-item>
              <el-form-item label="电子邮箱: ">
                <el-input v-model="registerForm.email" placeholder="请输入你的电子邮箱"/>
              </el-form-item>
              <el-form-item label="密码: ">
                <el-input v-model="registerForm.password" placeholder="请输入密码" type="password" show-password/>
              </el-form-item>
              <el-form-item label="确认密码: ">
                <el-input v-model="registerForm.confirmPassword" placeholder="请再次输入密码" type="password" show-password/>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="sendRegisterForm">注册</el-button>
                <el-button @click="cancelRegister">取消</el-button>
              </el-form-item>
            </el-form>
          </el-card>
        </el-col>
      </el-row>
    </el-main>
  </div>
</template>

<script lang="ts" setup>
const registerForm = reactive({
  phoneNumber: '',
  email: '',
  password: '',
  confirmPassword: '',
});

const sendRegisterForm = () => {
  console.log(registerForm);
  ElMessage.success('注册成功');
};

const cancelRegister = () => {
  // 这里实现取消逻辑，并清空所有输入框内容
  console.log('取消按钮被点击', registerForm);
  // 清空表单字段
  registerForm.phoneNumber = '';
  registerForm.email = '';
  registerForm.password = '';
  registerForm.confirmPassword = '';
};
</script>

<style scoped>

</style>