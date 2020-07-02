import { UserState } from './../../store/states/user.state';


export interface IUserListRequest {
    totalCount: number;
    next: string;
    previous: string;
    payload: UserState[];
}