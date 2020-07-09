import { TestBed } from '@angular/core/testing';

import { CentService } from './cent.service';

describe('CentService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CentService = TestBed.get(CentService);
    expect(service).toBeTruthy();
  });
});
