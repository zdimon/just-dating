import { Action } from '@ngrx/store';
import { UserState } from '../states/user.state';

export enum UserActionTypes {
  UpdateUsers = '[User] Update users',
  UpdateUser = '[User] Update One user',
  UpdateUsersDone = '[User] Update users DONE!!!',
}

export class UpdateUsers implements Action {
  readonly type = UserActionTypes.UpdateUsers;
  constructor(public payload: UserState[]) {}
}

export class UpdateUser implements Action {
  readonly type = UserActionTypes.UpdateUser;
  constructor(public payload: UserState) {}
}

export class UpdateUsersDone implements Action {
  readonly type = UserActionTypes.UpdateUsersDone;
}



export type UserActionsUnion =
UpdateUsers |
UpdateUser |
UpdateUsersDone;