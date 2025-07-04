<template>
  <div id="app">
    <h1>Industrial Fault Detection</h1>
    <input type="file" @change="uploadFile" />
    <div>{{ result }}</div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      result: ''
    }
  },
  methods: {
    async uploadFile(event) {
      const file = event.target.files[0];
      const formData = new FormData();
      formData.append('file', file);
      const response = await axios.post('/api/predict', formData);
      this.result = response.data;
    }
  }
}
</script>
