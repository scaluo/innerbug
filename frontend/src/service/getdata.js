import axios from 'axios'
import store from '../store/index'
const qs = require('qs')
const rooturl = "http://localhost:5000/api"
const api = {
  async get (url, data) {
    try {
      let res = await axios.get(rooturl+url, {params: data})
      res = res.data
      return new Promise((resolve) => {
        if (res.code === 0) {
          resolve(res)
        } else {
          resolve(res)
        }
      })
    } catch (err) {
      alert('服务器出错')
      console.log(err)
    }
  },
  async post (url, data) {
    try {
      let res = await axios.post(rooturl+url, qs.stringify(data),{validateStatus: function (status) {
        return status >= 200 && status < 500; // default
      }})
      
        res = res.data
        return new Promise((resolve, reject) => {
          
          if (!res.hasOwnProperty("errorCode")) {
            resolve(res)
          } else {
            alert(res.errorMessage)
            reject(res)
          } 
        })
     
    } catch (err) {
      // return (e.message)
      alert(err)
      console.log(err)
    }
  },

  async getwithauth (url, data) {
    try {
      let res = await axios.get(rooturl+url, {params: data,headers:{'Authorization':store.state.token}})
      res = res.data
      return new Promise((resolve) => {
        if (res.code === 0) {
          resolve(res)
        } else {
          resolve(res)
        }
      })
    } catch (err) {
      alert('服务器出错')
      console.log(err)
    }
  },
  async postwithauth (url, data) {
    try {
      let res = await axios.post(rooturl+url, qs.stringify(data),{headers:{'Authorization':store.state.token}},{validateStatus: function (status) {
        return status >= 200 && status < 500; // default
      }})
      
        res = res.data
        return new Promise((resolve, reject) => {
          
          if (!res.hasOwnProperty("errorCode")) {
            resolve(res)
          } else {
            alert(res.errorMessage)
            reject(res)
          } 
        })
     
    } catch (err) {
      // return (e.message)
      alert(err)
      console.log(err)
    }
  }
}

function login(username,password)
{
    return api.post('/login',{'loginname':username,'password':password});
}

function changepassword(oldpassword,newpassword)
{
    return api.postwithauth('/changepass',{'oldpassword':oldpassword,'newpassword':newpassword});
}

function getprojectlist()
{
  return api.getwithauth('/projects');
}

function addproject(projectname)
{
    return api.postwithauth('/addproject',{'projectname':projectname});
}

function addbug(title,level,prj,content)
{
  return api.postwithauth('/addbug',{'title':title,'level':level,'prj':prj,'content':content})
}

function getbuglist(prjid)
{

  return api.getwithauth('/bugs/'+prjid);
}

function getbug(id)
{
  return api.getwithauth('/bug/'+id);
}

function setbugstatus(id,status)
{
  return api.postwithauth('/setbugstatus',{'id':id,'status':status});
}

function updatebug(id,title,prj,level,content)
{
  return api.postwithauth('/updatebug',{'id':id,'title':title,'level':level,'prj':prj,'content':content})
}

function delbug(id)
{
  return api.postwithauth('/delbug',{'id':id})
}

function delprj(id)
{
  return api.postwithauth('/delprj',{'id':id})
}

function getuserlist()
{
  return api.getwithauth('/users');
}

function deluser(id)
{
  return api.postwithauth('/deluser',{'id':id})
}

function adduser(username,loginname,password,isadmin)
{
  return api.postwithauth('/adduser',{'username':username,'loginname':loginname,'password':password,'isadmin':isadmin})
}

var authID = store.state.Authorization;

export {login,
        changepassword,
        addproject,
        getprojectlist,
        getbuglist,
        addbug,
        getbug,
        setbugstatus,
        updatebug,
        delbug,
        delprj,
        getuserlist,
        deluser,
        adduser,
        authID};