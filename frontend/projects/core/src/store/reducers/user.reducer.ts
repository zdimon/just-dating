import {EntityAdapter, createEntityAdapter} from '@ngrx/entity';

import { UserState, UserListState, defaultState } from '../states/user.state';
import * as usersActions from '../actions/user.action';

export const adapter: EntityAdapter<UserState> = createEntityAdapter<UserState>(defaultState);

export const initialState: UserListState = adapter.getInitialState();

export function UserReducer(state = initialState, action: usersActions.UserActionsUnion) {

  switch (action.type) {

    case usersActions.UserActionTypes.UpdateUsers:
      return adapter.addMany(action.payload, {...state});

    case usersActions.UserActionTypes.UpdateUser:
      return adapter.upsertOne(action.payload, {...state});

    default:
      return state;
  }
}