export interface BasicOrg {
    name: string;
    desc: string;
    lat: number;
    lng: number;
    img_url: string;
}

export interface Org extends BasicOrg {
    id: number;
}

export interface BasicUser {
    username: string;
    email: string;
    password: string;
    number?: number;
    lat: number;
    lng: number;
    car_capacity: number;
}

export interface User {
    car_capacity: number;
    id: number;
    latitude: number;
    longitude: number;
    name: string;
}