import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';

@Injectable()
export class service_python {



  constructor(private http: HttpClient) {}
  routh_ans(inputData: any): Observable<any> {
    return this.http.post('http://localhost:5000/routh', inputData );
  }
  
}