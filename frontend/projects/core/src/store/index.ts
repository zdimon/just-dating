
import { ActionReducerMap } from '@ngrx/store';

import { SessionState } from './states/session.state';
import {SessionReducer} from './reducers/session.reducer';


export interface State {
    session: SessionState;
}

export const reducers: ActionReducerMap<State> = {
    session: SessionReducer,
  };
