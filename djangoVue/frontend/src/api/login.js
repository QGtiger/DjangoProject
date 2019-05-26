import request from '@/libs/request'
import qs from 'qs'

export function doLogin (username, password) {
  let data = {
    username,
    password
  }
  data = qs.stringify(data)
  return request({
    url: '/backend/login',
    method: 'post',
    data
  })
}