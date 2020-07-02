import { UserListState } from '../states/user.state';
import { createSelector, createFeatureSelector } from '@ngrx/store';

export const getUserListStateSelector = createFeatureSelector<UserListState>('users');

export const selectUsersIds = createSelector(getUserListStateSelector, (state: UserListState) => state.ids);


export const selectUserList = createSelector(
    getUserListStateSelector,
    (state: UserListState) => state.entities
);

export const selectUsersArray = createSelector(
    selectUsersIds,
    selectUserList,
    (ids: any, users: any) => {
        return ids.map((id) => users[id]);
      }
);

