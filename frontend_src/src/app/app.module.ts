import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { shapes } from 'konva/lib/Shape';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { service_java } from './service_java';
import { service_python } from './service_python';
import { CommonModule } from '@angular/common';

@NgModule({
  declarations: [
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    CommonModule,



  ],
  providers: [service_java,service_python],
  bootstrap: [AppComponent]
})
export class AppModule { }
