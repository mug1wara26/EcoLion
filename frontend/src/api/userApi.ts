import {BasicUser, User} from "@/schema/types";
import {get_req, post_req} from "@/api/api";

export const register = (basicUser: BasicUser): Promise<Response> => {
    return new Promise<Response>(resolve => {
        post_req('/user/register', {user: basicUser}).then(res => resolve(res))
    })
}

export const login = (basicUser: BasicUser): Promise<Response> => {
    return new Promise<Response>(resolve => {
        post_req('/user/login', {user: basicUser}).then(res => resolve(res))
    })
}

export const getUser = (): Promise<User> => {
    return new Promise<User>(resolve => {
        get_req('/user/').then(res => {
            if (res.status === 200) res.json().then(data => resolve(data.user))
            else resolve({} as User)
        })
    })
}