#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Tax Auditor"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.common.constants import HttpClientCode, HttpServerCode, ApiResponse
from app.common.strings import HttpClientErrorMessage, HttpServerErrorMessage

error = APIRouter()


# Custom exception handler for 401 (Unauthorized)
@error.exception_handler(HTTPException)
async def unauthorized_exception_handler(request, exc):
    if exc.status_code is HttpClientCode.BAD_REQUEST:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.BAD_REQUEST},
            status_code=HttpClientCode.BAD_REQUEST,
        )
    elif exc.status_code is HttpClientCode.UNAUTHORIZED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.UNAUTHORIZED},
            status_code=HttpClientCode.UNAUTHORIZED,
        )
    elif exc.status_code is HttpClientCode.PAYMENT_REQUIRED:
        return JSONResponse(
            content={
                ApiResponse.ERROR: HttpClientErrorMessage.PAYMENT_REQUIRED_EXPERIMENTAL
            },
            status_code=HttpClientCode.PAYMENT_REQUIRED,
        )
    elif exc.status_code is HttpClientCode.FORBIDDEN:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.FORBIDDEN},
            status_code=HttpClientCode.FORBIDDEN,
        )
    elif exc.status_code is HttpClientCode.NOT_FOUND:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.NOT_FOUND},
            status_code=HttpClientCode.NOT_FOUND,
        )
    elif exc.status_code is HttpClientCode.METHOD_NOT_ALLOWED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.METHOD_NOT_ALLOWED},
            status_code=HttpClientCode.METHOD_NOT_ALLOWED,
        )
    elif exc.status_code is HttpClientCode.NOT_ACCEPTABLE:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.NOT_ACCEPTABLE},
            status_code=HttpClientCode.NOT_ACCEPTABLE,
        )
    elif exc.status_code is HttpClientCode.PROXY_AUTHENTICATION_REQUIRED:
        return JSONResponse(
            content={
                ApiResponse.ERROR: HttpClientErrorMessage.PROXY_AUTHENTICATION_REQUIRED
            },
            status_code=HttpClientCode.PROXY_AUTHENTICATION_REQUIRED,
        )
    elif exc.status_code is HttpClientCode.REQUEST_TIMEOUT:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.REQUEST_TIMEOUT},
            status_code=HttpClientCode.REQUEST_TIMEOUT,
        )
    elif exc.status_code is HttpClientCode.CONFLICT:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.CONFLICT},
            status_code=HttpClientCode.CONFLICT,
        )
    elif exc.status_code is HttpClientCode.GONE:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.GONE},
            status_code=HttpClientCode.GONE,
        )
    elif exc.status_code is HttpClientCode.LENGTH_REQUIRED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.LENGTH_REQUIRED},
            status_code=HttpClientCode.LENGTH_REQUIRED,
        )
    elif exc.status_code is HttpClientCode.PRECONDITION_FAILED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.PRECONDITION_FAILED},
            status_code=HttpClientCode.PRECONDITION_FAILED,
        )
    elif exc.status_code is HttpClientCode.PAYLOAD_TOO_LARGE:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.PAYLOAD_TOO_LARGE},
            status_code=HttpClientCode.PAYLOAD_TOO_LARGE,
        )
    elif exc.status_code is HttpClientCode.URI_TOO_LONG:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.URI_TOO_LONG},
            status_code=HttpClientCode.URI_TOO_LONG,
        )
    elif exc.status_code is HttpClientCode.UNSUPPORTED_MEDIA_TYPE:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.UNSUPPORTED_MEDIA_TYPE},
            status_code=HttpClientCode.UNSUPPORTED_MEDIA_TYPE,
        )
    elif exc.status_code is HttpClientCode.RANGE_NOT_SATISFIABLE:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.RANGE_NOT_SATISFIABLE},
            status_code=HttpClientCode.RANGE_NOT_SATISFIABLE,
        )
    elif exc.status_code is HttpClientCode.EXPECTATION_FAILED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.EXPECTATION_FAILED},
            status_code=HttpClientCode.EXPECTATION_FAILED,
        )
    elif exc.status_code is HttpClientCode.IM_A_TEAPOT:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.IM_A_TEAPOT},
            status_code=HttpClientCode.IM_A_TEAPOT,
        )
    elif exc.status_code is HttpClientCode.MISDIRECTED_REQUEST:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.MISDIRECTED_REQUEST},
            status_code=HttpClientCode.MISDIRECTED_REQUEST,
        )
    elif exc.status_code is HttpClientCode.UNPROCESSABLE_CONTENT:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.UNPROCESSABLE_CONTENT},
            status_code=HttpClientCode.UNPROCESSABLE_CONTENT,
        )
    elif exc.status_code is HttpClientCode.LOCKED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.LOCKED},
            status_code=HttpClientCode.LOCKED,
        )
    elif exc.status_code is HttpClientCode.FAILED_DEPENDENCY:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.FAILED_DEPENDENCY},
            status_code=HttpClientCode.FAILED_DEPENDENCY,
        )
    elif exc.status_code is HttpClientCode.TOO_EARLY:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.TOO_EARLY_EXPERIMENTAL},
            status_code=HttpClientCode.TOO_EARLY,
        )
    elif exc.status_code is HttpClientCode.UPGRADE_REQUIRED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.UPGRADE_REQUIRED},
            status_code=HttpClientCode.UPGRADE_REQUIRED,
        )
    elif exc.status_code is HttpClientCode.PRECONDITION_REQUIRED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.PRECONDITION_REQUIRED},
            status_code=HttpClientCode.PRECONDITION_REQUIRED,
        )
    elif exc.status_code is HttpClientCode.TOO_MANY_REQUESTS:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpClientErrorMessage.TOO_MANY_REQUESTS},
            status_code=HttpClientCode.TOO_MANY_REQUESTS,
        )
    elif exc.status_code is HttpClientCode.REQUEST_HEADER_FIELDS_TOO_LARGE:
        return JSONResponse(
            content={
                ApiResponse.ERROR: HttpClientErrorMessage.REQUEST_HEADER_FIELDS_TOO_LARGE
            },
            status_code=HttpClientCode.REQUEST_HEADER_FIELDS_TOO_LARGE,
        )
    elif exc.status_code is HttpClientCode.UNAVAILABLE_FOR_LEGAL_REASONS:
        return JSONResponse(
            content={
                ApiResponse.ERROR: HttpClientErrorMessage.UNAVAILABLE_FOR_LEGAL_REASONS
            },
            status_code=HttpClientCode.UNAVAILABLE_FOR_LEGAL_REASONS,
        )
    elif exc.status_code is HttpServerCode.INTERNAL_SERVER_ERROR:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpServerErrorMessage.INTERNAL_SERVER_ERROR},
            status_code=HttpServerCode.INTERNAL_SERVER_ERROR,
        )
    elif exc.status_code is HttpServerCode.NOT_IMPLEMENTED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpServerErrorMessage.NOT_IMPLEMENTED},
            status_code=HttpServerCode.NOT_IMPLEMENTED,
        )
    elif exc.status_code is HttpServerCode.BAD_GATEWAY:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpServerErrorMessage.BAD_GATEWAY},
            status_code=HttpServerCode.BAD_GATEWAY,
        )
    elif exc.status_code is HttpServerCode.SERVICE_UNAVAILABLE:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpServerErrorMessage.SERVICE_UNAVAILABLE},
            status_code=HttpServerCode.SERVICE_UNAVAILABLE,
        )
    elif exc.status_code is HttpServerCode.GATEWAY_TIMEOUT:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpServerErrorMessage.GATEWAY_TIMEOUT},
            status_code=HttpServerCode.GATEWAY_TIMEOUT,
        )
    elif exc.status_code is HttpServerCode.HTTP_VERSION_NOT_SUPPORTED:
        return JSONResponse(
            content={
                ApiResponse.ERROR: HttpServerErrorMessage.HTTP_VERSION_NOT_SUPPORTED
            },
            status_code=HttpServerCode.HTTP_VERSION_NOT_SUPPORTED,
        )
    elif exc.status_code is HttpServerCode.VARIANT_ALSO_NEGOTIATES:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpServerErrorMessage.VARIANT_ALSO_NEGOTIATES},
            status_code=HttpServerCode.VARIANT_ALSO_NEGOTIATES,
        )
    elif exc.status_code is HttpServerCode.INSUFFICIENT_STORAGE:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpServerErrorMessage.INSUFFICIENT_STORAGE},
            status_code=HttpServerCode.INSUFFICIENT_STORAGE,
        )
    elif exc.status_code is HttpServerCode.LOOP_DETECTED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpServerErrorMessage.LOOP_DETECTED},
            status_code=HttpServerCode.LOOP_DETECTED,
        )
    elif exc.status_code is HttpServerCode.NOT_EXTENDED:
        return JSONResponse(
            content={ApiResponse.ERROR: HttpServerErrorMessage.NOT_EXTENDED},
            status_code=HttpServerCode.NOT_EXTENDED,
        )
    elif exc.status_code is HttpServerCode.NETWORK_AUTHENTICATION_REQUIRED:
        return JSONResponse(
            content={
                ApiResponse.ERROR: HttpServerErrorMessage.NETWORK_AUTHENTICATION_REQUIRED
            },
            status_code=HttpServerCode.NETWORK_AUTHENTICATION_REQUIRED,
        )
    return exc


# Custom exception handler for 500 (Internal Server Error)
@error.exception_handler(HTTPException)
async def internal_server_error_handler(request, exc):
    if exc.status_code is 500:
        return JSONResponse(
            content={ApiResponse.ERROR: "Internal server error"}, status_code=500
        )
    return exc
