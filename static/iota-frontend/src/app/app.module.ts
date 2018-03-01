import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
//import { NgMaterial} from '@angular/core';
import { AppComponent } from './app.component';
import { LightsComponent } from './lights/lights.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatCardModule, MatButtonModule, MatSliderModule, MatListModule,
MatGridListModule, MatTableModule } from '@angular/material';
import { HttpModule } from '@angular/http';
import { FlexLayoutModule} from '@angular/flex-layout';


@NgModule({
  declarations: [
    AppComponent,
    LightsComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatCardModule,
    MatButtonModule,
    MatSliderModule,
    MatListModule,
    MatGridListModule,
    //NgMaterial,
    FlexLayoutModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
