import {BasicOrg, Org} from "@/schema/types";
import {get_req, post_req} from "@/api/api";

export const createOrg = (basicOrg: BasicOrg): Promise<number> => {
    return new Promise<number>((resolve, reject) => {
        post_req('/community/create', {community: basicOrg}).then(res => {
            if (res.status === 200) res.json().then(data => resolve(data.community_id))
            else reject()
        }).catch(() => reject())
    })
}

export const getOrg = (org_id: number): Promise<Org> => {
    return new Promise<Org>(resolve => {
        get_req(`/community/${org_id}`).then(res => {
            if (res.status === 200) res.json().then(data => resolve(data.community as Org))
            else resolve({} as Org)
        })
    })
}

export const getOrgs = (): Promise<Array<Org>> => {
    return new Promise<Array<Org>>(resolve => {
        get_req('/community/get_communities').then(res => {
            if (res.status === 200) res.json().then(data => resolve(data.communities))
            else resolve([])
        })
    })
}