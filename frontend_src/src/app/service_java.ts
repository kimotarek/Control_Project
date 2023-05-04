import { Injectable } from "@angular/core"
import { HttpClient } from '@angular/common/http';
import { Observable } from "rxjs";

// import {class you made}
@Injectable({
  providedIn: 'root'
})


export class service_java {
  //private apiServerUrl = 'http://localhost:8080';
  constructor(private http: HttpClient) { }


public getAnswer(added:any,s:any,e:any):Observable<any>{
  return this.http.post<any>(`http://localhost:8080/addshape/${s}/${e}`, added);
}


}
