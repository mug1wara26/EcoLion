import {User} from "@/schema/types";
import {get_req} from "@/api/api";

export const getCarpoolUsers = (): Promise<Array<Array<User>>> => {
    return new Promise<Array<Array<User>>>(resolve => {
        get_req('/carpool/users').then(res => {
            if (res.status===200) res.json().then(data => resolve(data))
            else resolve([])
        })
    })
}