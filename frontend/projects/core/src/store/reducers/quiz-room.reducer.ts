import { QuizRoomActionTypes } from './../actions/quiz-room.action';
import {EntityAdapter, createEntityAdapter} from '@ngrx/entity';

import * as Actions from '../actions/quiz-room.action';
import {QuizRoomState, QuizRoomListState, defaultState} from '../states/quiz-room.state';

export const adapter: EntityAdapter<QuizRoomState> = createEntityAdapter<QuizRoomState>();

export const initialState: QuizRoomListState = adapter.getInitialState(defaultState);

export function QuizRoomReducer(state = initialState, action: Actions.ActionsUnion) {

    switch (action.type) {

        case Actions.QuizRoomActionTypes.UpdateQuizRoom:

          return adapter.upsertOne(action.payload, {...state});

        default:
        return state;

    }
}
