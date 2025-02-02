#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from dataclasses import dataclass


@dataclass(frozen=True)
class HttpInfoMessage:
    """dataclass HttpInfoMessage contains for Http Infomation Message."""

    CONTINUE = "This interim response indicates that the client should continue the request or ignore the response if the request is already finished."
    SWITCHING_PROTOCOLS = "This code is sent in response to an Upgrade request header from the client and indicates the protocol the server is switching to."
    PROCESSING = "This code indicates that the server has received and is processing the request, but no response is available yet."
    EARLY_HINTS = "This status code is primarily intended to be used with the Link header, letting the user agent start preloading resources while the server prepares a response or preconnect to an origin from which the page will need resources."


@dataclass(frozen=True)
class HttpSuccessMessage:
    """dataclass HttpSuccessMessage contains for Http Success Message."""

    OK = "The request succeeded."
    OK_GET = "The request succeeded. The resource has been fetched and transmitted in the message body."
    OK_HEAD = "The request succeeded. The representation headers are included in the response without any message body."
    OK_PUT_OR_POST = "The request succeeded. The resource describing the result of the action is transmitted in the message body."
    OK_TRACE = "The request succeeded. The message body contains the request message as received by the server."
    CREATED = "The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests."
    ACCEPTED = "The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for batch processing."
    NON_AUTHORITATIVE_INFORMATION = "This response code means the returned metadata is not exactly the same as is available from the origin server, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the 200 OK response is preferred to this status."
    NO_CONTENT = "There is no content to send for this request, but the headers may be useful. The user agent may update its cached headers for this resource with the new ones."
    RESET_CONTENT = (
        "Tells the user agent to reset the document which sent this request."
    )
    PARTIAL_CONTENT = "This response code is used when the Range header is sent from the client to request only part of a resource."
    MULTI_STATUS = "Conveys information about multiple resources, for situations where multiple status codes might be appropriate."
    ALREADY_REPORTED = "Used inside a <dav:propstat> response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection."
    IM_USED = "The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance."


@dataclass(frozen=True)
class HttpRedirectMessage:
    """dataclass HttpRedirectMessage contains for Http Redirect Message."""

    MULTIPLE_CHOICES = "The request has more than one possible response. The user agent or user should choose one of them. (There is no standardized way of choosing one of the responses, but HTML links to the possibilities are recommended so the user can pick.)"
    MOVED_PERMANENTLY = "The URL of the requested resource has been changed permanently. The new URL is given in the response."
    FOUND = "This response code means that the URI of requested resource has been changed temporarily. Further changes in the URI might be made in the future. Therefore, this same URI should be used by the client in future requests."
    SEE_OTHER = "The server sent this response to direct the client to get the requested resource at another URI with a GET request."
    NOT_MODIFIED = "This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response."
    USE_PROXY_DEPRECATED = "Defined in a previous version of the HTTP specification to indicate that a requested response must be accessed by a proxy. It has been deprecated due to security concerns regarding in-band configuration of a proxy."
    UNUSED = "This response code is no longer used; it is just reserved. It was used in a previous version of the HTTP/1.1 specification."
    TEMPORARY_REDIRECT = "The server sends this response to direct the client to get the requested resource at another URI with the same method that was used in the prior request. This has the same semantics as the 302 Found HTTP response code, with the exception that the user agent must not change the HTTP method used: if a POST was used in the first request, a POST must be used in the second request."
    PERMANENT_REDIRECT = "This means that the resource is now permanently located at another URI, specified by the Location: HTTP Response header. This has the same semantics as the 301 Moved Permanently HTTP response code, with the exception that the user agent must not change the HTTP method used: if a POST was used in the first request, a POST must be used in the second request."


@dataclass(frozen=True)
class HttpClientErrorMessage:
    """dataclass HttpClientErrorMessage contains for Http client error Message."""

    BAD_REQUEST = "The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing)."
    UNAUTHORIZED = "Although the HTTP standard specifies 'unauthorized', semantically this response means 'unauthenticated'. That is, the client must authenticate itself to get the requested response."
    PAYMENT_REQUIRED_EXPERIMENTAL = "This response code is reserved for future use. The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists."
    FORBIDDEN = "The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server."
    NOT_FOUND = "The server cannot find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web."
    METHOD_NOT_ALLOWED = "The request method is known by the server but is not supported by the target resource. For example, an API may not allow calling DELETE to remove a resource."
    NOT_ACCEPTABLE = "This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent."
    PROXY_AUTHENTICATION_REQUIRED = "This is similar to 401 Unauthorized but authentication is needed to be done by a proxy."
    REQUEST_TIMEOUT = "This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message."
    CONFLICT = "This response is sent when a request conflicts with the current state of the server."
    GONE = "This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Clients are expected to remove their caches and links to the resource. The HTTP specification intends this status code to be used for 'limited-time, promotional services'. APIs should not feel compelled to indicate resources that have been deleted with this status code."
    LENGTH_REQUIRED = "Server rejected the request because the Content-Length header field is not defined and the server requires it."
    PRECONDITION_FAILED = "The client has indicated preconditions in its headers which the server does not meet."
    PAYLOAD_TOO_LARGE = "Request entity is larger than limits defined by server. The server might close the connection or return an Retry-After header field."
    URI_TOO_LONG = "The URI requested by the client is longer than the server is willing to interpret."
    UNSUPPORTED_MEDIA_TYPE = "The media format of the requested data is not supported by the server, so the server is rejecting the request."
    RANGE_NOT_SATISFIABLE = "The range specified by the Range header field in the request cannot be fulfilled. It's possible that the range is outside the size of the target URI's data."
    EXPECTATION_FAILED = "This response code means the expectation indicated by the Expect request header field cannot be met by the server."
    IM_A_TEAPOT = "The server refuses the attempt to brew coffee with a teapot."
    MISDIRECTED_REQUEST = "The request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI."
    UNPROCESSABLE_CONTENT = "The request was well-formed but was unable to be followed due to semantic errors."
    LOCKED = "The resource that is being accessed is locked."
    FAILED_DEPENDENCY = "The request failed due to failure of a previous request."
    TOO_EARLY_EXPERIMENTAL = "Indicates that the server is unwilling to risk processing a request that might be replayed."
    UPGRADE_REQUIRED = "The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. The server sends an Upgrade header in a 426 response to indicate the required protocol(s)."
    PRECONDITION_REQUIRED = "The origin server requires the request to be conditional. This response is intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict."
    TOO_MANY_REQUESTS = "The user has sent too many requests in a given amount of time ('rate limiting')."
    REQUEST_HEADER_FIELDS_TOO_LARGE = "The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields."
    UNAVAILABLE_FOR_LEGAL_REASONS = "The user agent requested a resource that cannot legally be provided, such as a web page censored by a government."


@dataclass(frozen=True)
class HttpServerErrorMessage:
    """dataclass HttpServerErrorMessage contains for Http Server error Message."""

    INTERNAL_SERVER_ERROR = (
        "The server has encountered a situation it does not know how to handle."
    )
    NOT_IMPLEMENTED = "The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD."
    BAD_GATEWAY = "This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response."
    SERVICE_UNAVAILABLE = "The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached."
    GATEWAY_TIMEOUT = "This error response is given when the server is acting as a gateway and cannot get a response in time."
    HTTP_VERSION_NOT_SUPPORTED = (
        "The HTTP version used in the request is not supported by the server."
    )
    VARIANT_ALSO_NEGOTIATES = "The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process."
    INSUFFICIENT_STORAGE = "The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request."
    LOOP_DETECTED = "The server detected an infinite loop while processing the request."
    NOT_EXTENDED = (
        "Further extensions to the request are required for the server to fulfill it."
    )
    NETWORK_AUTHENTICATION_REQUIRED = (
        "Indicates that the client needs to authenticate to gain network access."
    )


@dataclass(frozen=True)
class UserMessage:
    """dataclass UserMessage contains for User string Message."""

    USER_REGISTERED_SUCCESSFULLY = "User registered successfully"
    USER_LOGGED_OUT_SUCCESSFULLY = "Logged out successfully"
    USER_PROTECTED_ACCESS = "Protected data accessed"
    USER_LOGGED_IN_SUCCESSFULLY = "Login Successful"


@dataclass(frozen=True)
class UserErrorMessage:
    """dataclass UserErrorMessage contains for User error string Message."""

    USER_ALREADY_REGISTERED = "Email already registered"
    USER_INCORRECT_USER_OR_PASSWORD = "Incorrect username or password"
    USER_INVALID_AUTHENTICATION_SCHEME = "Invalid authentication scheme"
    USER_INVALID_AUTHENTICATION_HEADER = "Invalid authorization header"


@dataclass(frozen=True)
class TokenMessage:
    """dataclass TokenMessage contains for Token string Message."""

    TOKEN_SENT_SUCCESSFULLY = "Token sent successfully"


@dataclass(frozen=True)
class TokenErrorMessage:
    """dataclass TokenErrorMessage contains for Token error string Message."""

    TOKEN_EXPIRED = "Token has expired"
    TOKEN_INVALID = "Invalid token"
    TOKEN_BLACKLISTED = "Token is blacklisted"
    TOKEN_ALREADY_BLACKLISTED = "Token already blacklisted"
    TOKEN_EXPIRED_TYPE_REFRESH = "Refresh token has expired"
