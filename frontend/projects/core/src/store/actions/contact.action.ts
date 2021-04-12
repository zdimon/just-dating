import { Action } from '@ngrx/store';
import { ContactState } from '../states/contact.state';

export enum ContactActionTypes {
  UpdateContacts = '[Contact] Update contacts'
}

export class UpdateContacts implements Action {
  readonly type = ContactActionTypes.UpdateContacts;
  constructor(public payload: ContactState) {}
}

export type ActionsUnion =
UpdateContacts;