import { EntityState } from '@ngrx/entity';

export interface IUserState {
    id: number;
    username: string;
    gender: string;
    birthday: string;
    main_photo: string;
    is_online: boolean;
}

export class UserState implements IUserState {
    constructor(
        public id: number = 0,
        public username: string = 'undefined',
        public gender: string = 'undefined',
        public birthday: string = 'undefined',
        public main_photo: string = 'undefined',
        public is_online: boolean = false
        ) {


    }
}


export interface UserListState extends EntityState<UserState> {
}

export const defaultState = {
    
};