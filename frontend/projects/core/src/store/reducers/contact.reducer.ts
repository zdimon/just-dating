import * as Actions from '../actions/contact.action';
import { ContactState, defaultState } from './../states/contact.state';

export function ContactReducer(state: ContactState = defaultState, action: Actions.ActionsUnion) {

    switch (action.type) {

        case Actions.ContactActionTypes.UpdateContacts:

          return {
            ...action.payload
          };

          

        default:
        return state;

    }
}
