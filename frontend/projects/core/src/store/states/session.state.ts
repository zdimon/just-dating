/* author Dmitry Zharikov zdimon77@gmail.com */

import { UserState } from './user.state';

export interface SessionState {
    token: string;
    isAuth: boolean;
    user: UserState;
}

export const defaultState = {
    token: 'undefined',
    isAuth: false,
    user: new UserState()
};
