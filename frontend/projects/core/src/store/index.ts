import { ActionReducerMap } from '@ngrx/store';

import { SessionState } from './states/session.state';
import {SessionReducer} from './reducers/session.reducer';

import { UserReducer } from './reducers/user.reducer';
import { UserListState } from './states/user.state';

export interface State {
    session: SessionState;
    users: UserListState;
}

export const reducers: ActionReducerMap<State> = {
    session: SessionReducer,
    users: UserReducer
  };
