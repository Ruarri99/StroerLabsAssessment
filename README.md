# StroerLabsAssessment
A Python exercise requested by Ströer Labs to assess my skills.

Approach and Rationale:
 - I wasn't sure about the use of 3rd party libraries outside the common metrics library mentioned, so I opted to use Python standard libraries for the assessment.
 - The urllib.requests module was used for API call handling and http.server module was used to host the metrics and exchange rate endpoints.

Things I Would Add/Change:
 - I ran out of time writing unit tests for the server_manager and rates_manager modules, so I would like to have done a better job at unit testing.
 - Improve the error checking of the api endpoints I am hosting to give better error responses.
 - Would change the metrics evaluator function to not update the api metric counts when it uses the cache.
