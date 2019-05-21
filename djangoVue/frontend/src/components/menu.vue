<template>
    <div>
    <Menu mode="horizontal" :theme="theme1" active-name="1">
        <router-link :to="'/'">
            <MenuItem name="1">
                <Icon type="ios-paper" />
                首页
            </MenuItem>
        </router-link>
        <MenuItem name="2">
            <Icon type="ios-people" />
            用户管理
        </MenuItem>
        <Submenu name="3">
            <template slot="title">
                <Icon type="ios-stats" />
                统计分析
            </template>
            <MenuGroup title="使用">
                <router-link :to="'login'"><MenuItem name="3-1">登录</MenuItem></router-link>
                <router-link :to="'register'"><MenuItem name="3-2">注册</MenuItem></router-link>
            </MenuGroup>
            <MenuGroup title="留存">
                <MenuItem name="3-4">用户留存</MenuItem>
                <MenuItem name="3-5">流失用户</MenuItem>
            </MenuGroup>
        </Submenu>
    </Menu>
    </div>
</template>
<script>
    export default {
        data () {
            return {
                theme1: 'dark'
            }
        }
    }
</script>
