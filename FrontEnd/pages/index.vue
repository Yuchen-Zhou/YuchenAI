<template>
  <div class="common-layout">
    <el-header>
      <Topbar />
    </el-header>
    <el-main>
      <carousel />
    </el-main>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
const response = ref(null);

onMounted(async () => {
  try {
    const res = await fetch('http://192.168.124.4:8000/hello', { method: 'GET' });
    if (res.ok) {
      response.value = await res.json();
      console.log(response.value);
    } else {
      console.error('Fetch error: ', res.status);
    }
  } catch (error) {
    console.error('Fetch error: ', error);
  }
});
</script>
