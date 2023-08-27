import Vue from "vue";
import {getCookie} from "typescript-cookie";

export const post_req = (url: string, body: any): Promise<Response> => {
    const token = getCookie('token') || ''
    return new Promise<Response>(resolve => {
        fetch(`${Vue.prototype.apiLink}${url}`, {
            method: 'POST',
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": token
            },
            body: JSON.stringify(body),
        }).then(res => resolve(res))
    })
}


export const get_req = (url: string): Promise<Response> => {
    const token = getCookie('token') || ''
    return new Promise<Response>(resolve => {
        fetch(`${Vue.prototype.apiLink}${url}`, {
            method: 'GET',
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": token
            },
        }).then(res => resolve(res))
    })
}