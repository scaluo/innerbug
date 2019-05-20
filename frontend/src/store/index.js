import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex);
//初始化时用sessionStore.getItem('token'),这样子刷新页面就无需重新登录
const state = {
  token: window.sessionStorage.getItem('token'),
  username: window.sessionStorage.getItem('username'),
  isadmin:window.sessionStorage.getItem('isadmin')
};

const mutations = {
  LOGIN: (state, data) => {
    //更改token的值
    state.token = data.access_token;
    state.username = data.user_name;
    state.isadmin = data.isadmin;
    window.sessionStorage.setItem('token', data.access_token);
    window.sessionStorage.setItem('username', data.user_name);
    window.sessionStorage.setItem('isadmin', data.isadmin);
  },
  LOGOUT: (state) => {
    //登出的时候要清除token
    state.token = null;
    window.sessionStorage.removeItem('token');
    window.sessionStorage.removeItem('username');
  },
  USERNAME: (state, data) => {
    //把用户名存起来
    state.username = data;
    window.sessionStorage.setItem('username', data);
  }
};

const actions = {
  UserLogin({ commit }, data){
    commit('LOGIN', data);
  },
  UserLogout({ commit }){
    commit('LOGOUT');
  },
  UserName({ commit }, data){
    commit('USERNAME', data);
  }
};

export default new Vuex.Store({
  state,
  mutations,
  actions
});