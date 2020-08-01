import * as Actions from '../actions/session.action';
import {SessionState, defaultState} from '../states/session.state';

export function SessionReducer(state: SessionState = defaultState, action: Actions.ActionsUnion) {

    switch (action.type) {

        case Actions.ActionTypes.Init:

          return {
            ...action.payload,
            isAuth: true
          };

          case Actions.ActionTypes.LogIn:

            return {
              ...action.payload,
              isAuth: true
            };

        case Actions.ActionTypes.LogOut:

            return {
                ...defaultState
            };

        default:
        return state;

    }
}
