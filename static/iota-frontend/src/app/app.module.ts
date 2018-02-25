import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgMaterial} from '@angular/core';
import { AppComponent } from './app.component';
import { LightsComponent } from './lights/lights.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatCardModule, MatButtonModule, MatSliderModule } from '@angular/material';
// import { HammertimeDirective } from './hammertime.directive';
import { HttpModule } from '@angular/http';

@NgModule({
  declarations: [
    AppComponent,
    LightsComponent,
    //HammertimeDirective
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatCardModule,
    MatButtonModule,
    MatSliderModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
