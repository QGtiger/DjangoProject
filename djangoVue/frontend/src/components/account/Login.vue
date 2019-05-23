<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div>
      <label for="username">Username</label>
      <Input v-model="username" placeholder="Enter name" id="username" style="width: auto"/>
    </div>
    <div>
      <label for="password">Password</label>
      <Input v-model="password" placeholder="Enter password" id="password" style="width: auto"/>
    </div>
    <br>
    <br>
    <Button type="primary" @click="handleLogin" key="login">登录</Button>
  </div>
</template>

<script>
import $ from "@/jquery";
import axios from "axios";
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      username: "",
      password: ""
    };
  },
  methods: {
    handleLogin() {
      var _this = this;
      var username = _this.username;
      var password = _this.password;
      if (!(username && password)) {
        this.$Modal.error({
          title: "错误",
          content: "用户名和密码不能为空"
        });
        return;
      }
      var data = {
        username: _this.username,
        password: _this.password
      };
      console.log(data);
      // jQuery.ajax({
      //   url: "http://127.0.0.1:8000/backend/login",
      //   type: "POST",
      //   data: data,
      //   dataType: 'json',
      //   success: function(e){
      //     _this.msg = e;
      //   }
      // })ma
      const _data = new FormData();
      _data.append("username", _this.username);
      _data.append("password", _this.password);
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/backend/login",
        data: _data,
        // withCredentials: true
      }).then(res => {
        console.log(res.data);
        _this.msg = res.data;
        const { sesssionid } = res.data;
        localStorage.setItem("sesssionid", sesssionid);
        document.cookie = `sesssionid=${sesssionid};`
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
