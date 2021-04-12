import {EntityAdapter, createEntityAdapter} from '@ngrx/entity';

import * as Actions from '../actions/quiz-message.action';
import {QuizMessageState, QuizMessageListState, defaultState} from '../states/quiz-message.state';

export const adapter: EntityAdapter<QuizMessageState> = createEntityAdapter<QuizMessageState>();

export const initialState: QuizMessageListState = adapter.getInitialState(defaultState);

export function QuizMessageReducer(state = initialState, action: Actions.ActionsUnion) {

    switch (action.type) {

        case Actions.QuizMessageActionTypes.UpdateQuizMessages:
          return adapter.upsertMany(action.payload, {...state });
        
        case Actions.QuizMessageActionTypes.UpdateQuizMessage:
          return adapter.upsertOne(action.payload, {...state });

        default:
        return state;

    }
}
